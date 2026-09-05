declare global {
    interface Window {
        pywebview: {
            api: {
                saveContent(content: string): Promise<void>;
            };
            state: {
                setTicker(s: string): void;
            };
        };
    }
}
export { };