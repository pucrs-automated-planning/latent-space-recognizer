require("antd/dist/antd.css");
import axios from "axios";
import { observer } from "mobx-react";
import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import AppStore from "./app.store";
import Send from "./components/routing/send";
import AppSession from "./session/app";
import PuzzleSelector from "./pages/puzzleSelector";
import Puzzle from "./pages/puzzle";

axios.interceptors.response.use(response => {
    console.log(`${response.config.method} ${response.config.url}: ${response.status}`);
    //console.log(JSON.stringify(response.data, null, 4));
    return response;
}, error => {
    console.log(`${error.config.method} ${error.config.url}: ${error.response.status}`);
    console.log(JSON.stringify(error.response.data, null, 2));
    return Promise.reject(error);
});


@observer
export default class App extends React.Component {

    store = new AppStore();
    appSession = AppSession.getInstance();

    constructor(props) {
        super(props);
        this.store.initialize();
    }


    render() {
        return (
            <Router>
                <div>
                    <Switch>
                        <Route exact path="/npuzzle/:start/:end" component={Puzzle} />
                        <Route exact path="/" component={PuzzleSelector} />
                    </Switch>
                    <Send />
                </div>
            </Router>
        );
    }
}