import React from 'react';
import './MovieList.css';

/* 
Below we use props.movies && props.movies.map()
map() will not run on undefined and will cause error
Using and condition we avoid if condition or try/except
With and props.movie must exist/evaluate to true or it exits
*/

function MovieList(props) {

    const movieClicked = (clickMovie) => (e) => {
        props.movieSelected(clickMovie)
        const showDetails = document.querySelector(".modal-details-wrapper")
        showDetails.style.display = 'block'
    };

    return (
        <div className="movie-listings">
            <h2>Moving Listings</h2>
            { props.movies && props.movies.map( movie => {
                return <p key={movie.id} onClick={movieClicked(movie)}>{movie.title}</p>
            })};
        </div>
    );
};

export default MovieList;
