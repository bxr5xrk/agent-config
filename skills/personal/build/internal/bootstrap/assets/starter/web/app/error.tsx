"use client";
import { useTransition } from "react";
import { Button } from "../components/button";
export default function ErrorPage({ retry }: { retry: () => void }) {
  const [pending, startTransition] = useTransition();
  return <section><h1>Could not load this page</h1><p role="alert">Your request failed. Try again.</p>
    <Button pending={pending} onClick={() => startTransition(retry)}>Retry</Button>
  </section>;
}
