import React from "react";

class Href extends React.Component {

    render() {
        window.location.href = this.props.href;
        return <div />;
    }
}

export default Href;