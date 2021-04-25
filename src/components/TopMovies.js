import React from 'react';
import './TopMovies.css';


function TopMovies(props) {
    return (
        <div className="top-movies-250">
            <h2>Top 250 Movies</h2>
            { props.movies && props.movies.map( movie => {
                return <p key={movie.id}>{movie.title}</p>
            })};
        </div>
    );
};

export default TopMovies;