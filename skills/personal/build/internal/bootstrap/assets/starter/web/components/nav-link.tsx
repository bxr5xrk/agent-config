"use client";
import Link, { useLinkStatus } from "next/link";
import { usePathname } from "next/navigation";
import type { ReactNode } from "react";
function Pending() {
  const { pending } = useLinkStatus();
  return <span role="status" aria-live="polite">{pending ? " — Loading…" : ""}</span>;
}
export function NavLink({ href, children }: { href: string; children: ReactNode }) {
  const pathname = usePathname();
  return <Link href={href} aria-current={pathname === href ? "page" : undefined}>{children}<Pending /></Link>;
}
