import { useEffect } from "react";

// 1. Safe access to the Python exposed API methods
export const Api = new Proxy({}, {
    get(t, p) {
        if (window.pywebview && window.pywebview.api) {
            return (window.pywebview.api as any)[p];
        }
        // Fallback function so React doesn't crash during early initialization
        return () => Promise.resolve(null);
    }
}) as typeof window.pywebview.api;

// 2. Safe access to pywebview's built-in State management
export const State = new Proxy({}, {
    get(t, p) {
        if (window.pywebview && window.pywebview.state) {
            return (window.pywebview.state as any)[p];
        }
        return undefined;
    },
    set(t, p, v) {
        if (window.pywebview) {
            (window.pywebview.state as any) ??= {};
            // Bypass custom assignments and write directly to the native pywebview proxy
            (window.pywebview.state as any)[p] = v;
            return true;
        }
        return false;
    }
}) as typeof window.pywebview.state;

// 3. Helper hook for handling async tasks cleanly inside components
export function useAsyncEffect(callback: () => Promise<void>, deps: React.DependencyList = []) {
    useEffect(() => {
        callback();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, deps);
}