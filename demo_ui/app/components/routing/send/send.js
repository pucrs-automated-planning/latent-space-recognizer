import React from "react";
import { observer } from "mobx-react";
import { Redirect } from "react-router";
import AppSession from "../../../session/app";

@observer
export default class Send extends React.Component {

    appSession = AppSession.getInstance();
    
    render() {
        if (this.appSession.to != null) {
            let to = this.appSession.to;
            console.log(`route ${to}`);
            return <Redirect push to={to} />;
        } else {
            return <div />;
        }
    }

    componentDidUpdate() {
        if (this.appSession.to != null) {
            this.appSession.to = null;
        }
    }
}