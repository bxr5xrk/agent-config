import type { Metadata } from "next";
import type { ReactNode } from "react";
import { NavLink } from "../components/nav-link";
import "./globals.css";
export const metadata: Metadata = {
  title: "Project scaffold",
  description: "Technical starter; replace with the agreed product.",
  robots: { index: false, follow: false },
};
export default function RootLayout({ children }: { children: ReactNode }) {
  return <html lang="en"><body>
    <a href="#main" className="skip">Skip to content</a>
    <header><nav aria-label="Main"><NavLink href="/">Home</NavLink><NavLink href="/status">Status</NavLink><NavLink href="/ui">Components</NavLink></nav></header>
    <main id="main">{children}</main>
  </body></html>;
}
