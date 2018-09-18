import React from "react";
import { observer } from "mobx-react";
import Header from "../../components/layout/header";
import NPuzzle from "../../components/npuzzle";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import styles from "./puzzle.scss";


@observer
export default class Puzzle extends React.Component {



    render() {
        let start = this.props.match ? this.props.match.params.start : "012345678";
        let end = this.props.match ? this.props.match.params.end : "012345678";
        return (
            <div>
                <Header />
                <div className={styles.card}>
                    <Card>
                        <CardContent>
                            <Typography variant="headline" component="h2">
                                {"Here's your puzzle"}
                            </Typography>
                            <NPuzzle start={start} end={end} />
                        </CardContent>
                    </Card>
                </div>
                <div className={styles.card}>
                    <Card>
                        <CardContent>
                            <Typography variant="headline" component="h2">
                                {"And your target!"}
                            </Typography>
                            <NPuzzle start={end} end={end} disabled={true} />
                        </CardContent>
                    </Card>
                </div>
                <div className={styles.card}>
                    <Card>
                        <CardContent>
                            <Typography variant="headline" component="h2">
                                {"Our best guess will be right here."}
                            </Typography>
                            <Typography color="textSecondary">
                                {"Coming soon!"}
                            </Typography>
                        </CardContent>
                    </Card>
                </div>
            </div>
        );
    }
}