import React from 'react';
import './TopMovies.css';


function TopMovies(props) {
        return (

                <div className="top-movies-250-wrapper">
                    <header className="header-top-movies">
                        <h2>Top 250 Movies</h2>
                        <div className="field-names">
                            <h3>Image</h3>
                            <h3>Rank - Title</h3>
                            <h3>Release Date</h3>
                            <h3>Rating</h3>
                        </div>
                    </header>
                    
                    { props.movies && props.movies.map( movie => {
                        return (
                            <ul className="top-movies-list">
                                
                                <li><img key={movie.id} src={movie.image} /></li>

                                <li key={movie.id}>{movie.rank}</li>
                                <li key={movie.id}>{movie.title}</li>
                                <li id="release" key={movie.id}>{movie.release_date}</li>
                                <li id="rating" key={movie.id}>{movie.rating}</li>
                            </ul>
                        )})}
                </div>
        
                
        );                  
};

export default TopMovies;