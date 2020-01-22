import React from 'react';
import ReactDOM from 'react-dom';
import { Widget } from 'rasa-webchat';


ReactDOM.render(
    <Widget
        initPayload={"/get_started"}
        socketUrl={"http://localhost:5005"}
        socketPath={"/socket.io/"}
        customData={{"language": "en"}}
        title={"Title"}
        customComponent={(messageData) => (
            <div><div>{messageData.key1}</div><div>{messageData.key2}</div></div>
        ) }
    />,
    document.querySelector('.container')
);
