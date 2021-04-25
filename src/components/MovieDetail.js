import React from 'react';
import './MovieDetail.css';


function MovieDetail(props) {
    return (
        <div className="modal-details-wrapper">
            <div className="modal-header">
                <h2>Movie Details</h2>
                <span id="x-selector">&Xfr;</span>
            </div>
            <div className="main-movie-section">
                <img
                    src="https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY67_CR0,0,45,67_AL_.jpg"
                    alt=""/> 

                <div className="movie-details">
                    <h3 id="movie-title">{props.movie && props.movie.title}</h3>
                    <p id="stats-height">{props.description && props.movie.description}</p>
                </div>
            </div>
            <div className="modal-movie-footer">
                <p>
                    Contact: email - ringler.brian@gmail.com<span> | </span> phone -
                    248-894-9966
                </p>
                <p><a href="https://github.com/brianRingler">GitHub</a></p>
            </div>
      </div>



    );
};

export default MovieDetail;