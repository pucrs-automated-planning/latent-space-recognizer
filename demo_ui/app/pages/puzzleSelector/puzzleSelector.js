import React from "react";
import { observer } from "mobx-react";
import Header from "../../components/layout/header";
import NPuzzle from "../../components/npuzzle";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import styles from "./puzzleSelector.scss";
import { Link } from "react-router-dom";


@observer
export default class PuzzleSelector extends React.Component {

    getPuzzle(key) {
        let start = "012345678".split("").sort(function () { return 0.5 - Math.random(); }).join("");
        let end = "012345678".split("").sort(function () { return 0.5 - Math.random(); }).join("");

        return (<div key={key} className={styles.puzzle}>
            <Link to={`/npuzzle/${start}/${end}`}>
                <NPuzzle disabled={true} start={end} end={end} />
            </Link>
        </div>);
    }

    render() {
        return (
            <div>
                <Header />
                <div className={styles.card}>
                    <Card>
                        <CardContent>
                            <Typography variant="headline" component="h2">
                                {"Please select a puzzle you would like to solve!"}
                            </Typography>
                            <Typography color="textSecondary">
                                {"Our AI will try to guess which result you're trying to obtain by watching you play."}
                            </Typography>
                        </CardContent>
                    </Card>
                </div>
                {[1, 2, 3, 4, 5, 6].map((x) => this.getPuzzle(x))}
            </div>
        );
    }
}