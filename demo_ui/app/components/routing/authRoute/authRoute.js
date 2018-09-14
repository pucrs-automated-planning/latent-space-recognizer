import React from "react";
import { observer } from "mobx-react";
import { Route, Redirect } from "react-router";

@observer
class AuthRoute extends React.Component {

    renderRoute(props) {
        if (!this.props.loggedIn || !this.props.allow()) {
            return <Redirect to={{ pathname: "/login", state: { from: props.location } }} />;
        } else {
            return <this.props.component match={props.match} location={props.location} />;
        }
    }

    render() {
        return <Route exact={this.props.exact} path={this.props.path} render={(props) => this.renderRoute(props)} />;
    }
}

AuthRoute.defaultProps = {
    allow: () => true,
    loggedIn: false,
    exact: false
};

export default AuthRoute;