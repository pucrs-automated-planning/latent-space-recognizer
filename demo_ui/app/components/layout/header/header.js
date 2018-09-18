import React from "react";
import { observer } from "mobx-react";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";

@observer
export default class Header extends React.Component {

    render() {
        return (
            <AppBar position="static" color="default">
                <Toolbar>
                    <Typography variant="title" color="inherit">
                        8-Puzzle
                    </Typography>
                </Toolbar>
            </AppBar>
        );
    }
}