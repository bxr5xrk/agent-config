// SDK-independent typed event contract; connect capture to one PostHog client.
export type ProductEvents = {
  primary_action_started: { surface: "public" | "app" };
  primary_action_completed: { surface: "public" | "app"; outcome: "created" | "updated" };
  primary_action_failed: { surface: "public" | "app"; code: "network" | "validation" | "unknown" };
};
export function createAnalytics(
  capture: (name: string, properties: Record<string, string>) => void,
  collectionAllowed: () => boolean,
) {
  return {
    track<K extends keyof ProductEvents>(name: K, properties: ProductEvents[K]) {
      if (!collectionAllowed()) { return; }
      // Explicitly pick allowed values; TS alone does not sanitize runtime input.
      const safe: Record<string, string> = {};
      if (properties.surface === "public" || properties.surface === "app") { safe.surface = properties.surface; }
      if (name === "primary_action_completed" && "outcome" in properties &&
          (properties.outcome === "created" || properties.outcome === "updated")) { safe.outcome = properties.outcome; }
      if (name === "primary_action_failed" && "code" in properties &&
          ["network", "validation", "unknown"].includes(properties.code)) { safe.code = properties.code; }
      capture(name, safe);
    },
  };
}
