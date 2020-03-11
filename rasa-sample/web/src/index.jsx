import React from 'react';
import ReactDOM from 'react-dom';
import { Widget } from 'rasa-webchat';
import FetchTest from './fetch';

//http://fsra-regbot-pilot-597364771.ap-southeast-1.elb.amazonaws.com:5005
ReactDOM.render(
    <div>
        <Widget
            initPayload={"/get_started"}
            socketUrl={"http://localhost:5005"}
            socketPath={"/socket.io/"}
            customData={{"language": "en","questionId": 7101,"applicationId": 1}}
            title={"Title"}
            customComponent={(messageData) => (
                <div><div>{messageData.key1}</div><div>{messageData.key2}</div></div>
            ) }
        />
        <FetchTest/>
    </div>,
    document.querySelector('.container')
);
