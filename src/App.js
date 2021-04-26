import React, { useEffect, useState } from 'react';
import MovieList from './components/MovieList';
import TopMovies from './components/TopMovies';
import MovieDetail from './components/MovieDetail';
import ComingSoon from './components/ComingSoon';
import './App.css';


function App() {

  // movies is the current state - setMovies is updated state
  const [movies, setMovies] = useState([]);
  // to start current state :selectedState will be null
  const [selectedMovie, setSelectedMovie] = useState(null);

  const localHost = 'http://127.0.0.1:8000/'
  const apiEndPoint = "api/movies/"
  
  useEffect(() => {
    fetch(localHost + apiEndPoint, {
      method: 'GET',
      headers: {
        'content-Type': 'application/json',
        // token is for user ringvision
        'Authorization': 'Token bba321ad567ecf4abc15bb7f072115bee0624bd3'
      }
    })
    .then( resp => resp.json())
    .then( resp => setMovies(resp))
    .catch( error => console.log(error))
  }, []);

  const movieClicked = (movie) => {
    setSelectedMovie(movie);
    console.log(movie);

  };

  return (
    <div className="app">
      <header className="app-header">
        <h1 className="main-header">RingVision Movie Ratings</h1>
      </header>
      <div className="main-layout">
          <TopMovies movies={movies} />
          <MovieList movies={movies} movieSelected={movieClicked}/>
          {/* note this is movie not movie(s) see movieClicked */}
          <MovieDetail movie={selectedMovie}/>
          <ComingSoon movies={movies}/>
      </div>
    </div>
  );
}

export default App;
