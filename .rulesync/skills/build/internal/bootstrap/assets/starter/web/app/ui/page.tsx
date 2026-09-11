import { Button } from "../../components/button";
import { LoadingState } from "../../components/loading-state";
export default function ComponentsPage() {
  return <><h1>Component states</h1><p className="muted">Technical samples; apply the chosen design tokens before building the product UI.</p>
    <section aria-labelledby="buttons"><h2 id="buttons">Actions</h2><div className="row"><Button>Default</Button><Button disabled>Unavailable</Button><Button pending>Save</Button></div></section>
    <section aria-labelledby="forms"><h2 id="forms">Field error</h2><label htmlFor="title">Title</label><input id="title" aria-invalid="true" aria-describedby="title-error" /><p id="title-error" className="error">Enter a title.</p></section>
    <section aria-labelledby="feedback"><h2 id="feedback">Feedback</h2><LoadingState /><p>No results yet.</p><p role="status">Changes saved.</p></section>
  </>;
}
