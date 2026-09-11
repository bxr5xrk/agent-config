// Illustrative boundary pattern. Supply the actual authorized loader when adapting.
import { Suspense } from "react";
type Item = { id: string; title: string };
async function Items({ load }: { load: () => Promise<Item[]> }) {
  const items = await load();
  return items.length ? <ul>{items.map(item => <li key={item.id}>{item.title}</li>)}</ul> : <p>No items yet.</p>;
}
export function ItemsPage({ loadAuthorizedItems }: { loadAuthorizedItems: () => Promise<Item[]> }) {
  return <><h1>Items</h1><Suspense fallback={<p role="status">Loading items…</p>}>
    <Items load={loadAuthorizedItems} />
  </Suspense></>;
}
// Bad: await loadAuthorizedItems() here before returning the Suspense boundary.
// The loader must authorize access before returning protected data.
