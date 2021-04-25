import React from 'react';
import './ComingSoon.css';


function ComingSoon(props) {
    return (

    <div className="coming-soon">
        <h2>Coming Soon</h2>
        { props.movies && props.movies.map( movie => {
            return <p key={movie.id}>{movie.title}</p>
        })};
    </div>
    

    );
};

export default ComingSoon;