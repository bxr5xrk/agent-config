import type { ComponentProps } from "react";
type Props = ComponentProps<"button"> & { pending?: boolean };
export function Button({ children, pending = false, disabled, type = "button", ...props }: Props) {
  return <button {...props} type={type} disabled={disabled || pending} aria-busy={pending}>
    {pending ? "Working… " : null}{children}
  </button>;
}
