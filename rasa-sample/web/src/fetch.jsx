import React from 'react';

const hostTest = "http://fsra-regbot-pilot-test-971690635.ap-southeast-1.elb.amazonaws.com";
const hostLocal = "http://localhost:8080";

class FetchTest extends React.Component {
    async handleFetch() {
        const params = {
            username: "sample@test.com",
            password: "password",
        };
        const result = await fetch(hostTest + "/api/admin/v1/login", {
            credentials: "same-origin",
            method: "post",
            headers: {
                "Authorization": "aaaa"
            },
            body: JSON.stringify(params)
        })
            .then(response => {
                const headers = {};
                for (let [key, value] of response.headers) {
                    headers[key] = value;
                }
                return {
                  headers: headers,
                  body: response.json(),
                };
            })
            .catch(error => console.log("Error", error)); // eslint-disable-line no-console

        console.log(result);
    }

    render() {
        return (
            <div>
                <button onClick={()=>this.handleFetch()}>Fetch</button>
            </div>
        );
    }
}

export default FetchTest;
