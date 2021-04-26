import React from 'react';
import './MovieList.css';

/* 
Below we use props.movies && props.movies.map()
map() will not run on undefined and will cause error
Using and condition we avoid if condition or try/except
With and props.movie must exist/evaluate to true or it exits
*/

function MovieList(props) {

    // see comment below detailing double arrow 
    const movieClicked = (clickMovie) => (e) => {
        props.movieSelected(clickMovie)
        const showDetails = document.querySelector(".modal-details-wrapper")
        showDetails.style.display = 'block'
    };

    return (
        <div className="movie-listings">
            <h2>Movie Listings</h2>
            { props.movies && props.movies.map( movie => {
                return <p key={movie.id} onClick={movieClicked(movie)}>{movie.title}</p>
            })};
        </div>
    );
};

export default MovieList;

/*
When a movie title is clicked the function movieClicked is triggered 
passing the argument 'movie' (which is the movie title) to that function. 

Within the App.js the movieSelected function is also triggered. This changes the current state defined as selectedState to setSlectedState to that active movie title. 

Answer from Krystian on why double arrow:
Basically whenever we click we generate a click event. This is captured by react and by default whenever we click on the element with an event listener. But when we need to pass some extra data with the click, our data cannot be directly inserted into a build-in event. So we capture that data and pass it to another function. That way we have a chain of events when browser click is registered, and also our function with extra data down the line. The syntax is weird and it takes time to get used to.
*/