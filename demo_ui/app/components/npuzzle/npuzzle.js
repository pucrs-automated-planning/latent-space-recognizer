import React from "react";
import { observer } from "mobx-react";
import Store from "./npuzzle.store";
import styles from "./npuzzle.scss";
import classnames from "classnames";

const entryStyles = function (x) {
    let r = {};
    r[styles.entry] = true;
    r[styles.highlight] = x.highlight;
    r[styles.correct] = x.correct;
    r[styles.hide] = x.hide;
    return r;
};

@observer
export default class NPuzzle extends React.Component {
    store = null;

    constructor(props) {
        super(props);
        this.store = new Store(this.props.start, this.props.end, this.props.callback);
    }

    renderPieces() {
        return this.store.model.map(x =>
            <div
                key={x.id}
                id={x.id}
                className={classnames(entryStyles(x))}
                draggable={x.id == "0" && !this.props.disabled}
                onDragStart={(e) => this.onDragStart(e, x)}
                onDragOver={(e) => this.onDragOver(e, x)}
                onDrop={(e) => this.onDrop(e, x)}
            >{x.id}</div>
        );
    }

    onDragOver(e) {
        e.preventDefault();
        e.dataTransfer.dropEffect = "move";
    }

    onDrop(e, x) {
        let y = JSON.parse(e.dataTransfer.getData("text/plain"));
        this.store.swap(x.id, y.id);
        this.store.highlight();
        this.store.check();
    }

    onDragStart(e, x) {
        e.dataTransfer.setData("text/plain", JSON.stringify(x));
        this.store.highlight(x.id);
    }

    render() {
        return (
            <div className={styles.grid}>
                {this.renderPieces()}
            </div>
        );
    }
}