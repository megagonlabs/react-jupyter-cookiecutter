import * as React from "react";
import * as ReactDOM from "react-dom";
export function bind(node, config) {
    return {
        create: (component, props, children) =>
            React.createElement(component, props, ...children),
        render: (element) => ReactDOM.render(element, node),
        unmount: () => ReactDOM.unmountComponentAtNode(node),
    };
}
import { Widget } from "./Widget";
export { Widget };
