import Fastify from "fastify";

export function buildApp({ logging = false }: { logging?: boolean } = {}) {
  const app = Fastify({
    logger: logging ? {
      redact: ["req.headers.authorization", "req.headers.cookie", "res.headers.set-cookie"],
    } : false,
    bodyLimit: 64 * 1024,
    requestTimeout: 10_000,
  });

  app.setErrorHandler((error, request, reply) => {
    const statusCode = typeof error === "object" && error !== null && "statusCode" in error ? error.statusCode : undefined;
    const status = typeof statusCode === "number" && statusCode >= 400 && statusCode < 500 ? statusCode : 500;
    // Do not log raw error messages: upstream exceptions can contain secrets.
    request.log.error({ requestId: request.id, status }, "Request failed");
    return reply.code(status).send({
      code: status === 400 ? "INVALID_REQUEST" : status < 500 ? "REQUEST_REJECTED" : "INTERNAL_ERROR",
      message: status < 500 ? "Request could not be accepted" : "Something went wrong",
      requestId: request.id,
    });
  });

  app.get("/health/live", {
    schema: { response: { 200: {
      type: "object", required: ["ok"], additionalProperties: false,
      properties: { ok: { type: "boolean" } },
    } } },
  }, async () => ({ ok: true }));

  // Demonstration contract only; replace with the agreed product's first journey.
  app.post<{ Body: { message: string } }>("/echo", {
    schema: {
      body: {
        type: "object", required: ["message"], additionalProperties: false,
        properties: { message: { type: "string", minLength: 1, maxLength: 200 } },
      },
      response: { 200: {
        type: "object", required: ["message"], additionalProperties: false,
        properties: { message: { type: "string" } },
      } },
    },
  }, async (request) => ({ message: request.body.message }));
  return app;
}
