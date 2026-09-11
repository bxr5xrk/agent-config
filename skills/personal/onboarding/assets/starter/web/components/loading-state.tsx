export function LoadingState() {
  return <div role="status" aria-live="polite">
    <p>Loading…</p><div className="skeleton" aria-hidden="true" />
  </div>;
}
