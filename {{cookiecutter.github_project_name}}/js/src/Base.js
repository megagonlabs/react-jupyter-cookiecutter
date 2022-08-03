import normalizeCss from "../node_modules/normalize.css/normalize.css";
import customCss from "../styles/custom.css";
export const Base = (props = {}) => {
    return (
        <div style={{ position: "relative" }}>
            <style>{normalizeCss}</style>
            <style>{customCss}</style>
            <div
                style={{
                    boxShadow:
                        "0 0 0 1px rgb(16 22 26 / 15%), 0 0 0 rgb(16 22 26 / 0%), 0 0 0 rgb(16 22 26 / 0%)",
                    borderRadius: 3,
                    padding: 0,
                    margin: 1,
                    overflow: "hidden",
                }}
            >
                {props.children}
            </div>
        </div>
    );
};
