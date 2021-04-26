import React from 'react';
import './MovieDetail.css';


function MovieDetail(props) {

    const hideDetailModal = () => {
        const hide = document.querySelector(".modal-details-wrapper");
        hide.style.display = 'none';
    }

    return (
        <div className="modal-details-wrapper">
            <div className="modal-header">
                <h2>Movie Details</h2>
                { /* <span onClick={hideDetailModal} id="x-selector">X</span> */ }
                <svg onClick={hideDetailModal}>
                    <circle cx="12" cy="12" r="11" stroke="black" stroke-width="2" fill="white" />
                    <path stroke="black" stroke-width="4" fill="none" d="M6.25,6.25,17.75,17.75" />
                    <path stroke="black" stroke-width="4" fill="none" d="M6.25,17.75,17.75,6.25" />
                </svg>
            </div>
            <div className="main-movie-section">
                <img
                    src="https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY67_CR0,0,45,67_AL_.jpg"
                    alt=""/> 

                <div className="movie-details">
                    <h3 id="movie-title">{props.movie && props.movie.title}</h3>
                    <h3 id="movie-desc">{props.description && props.movie.description}</h3>
                </div>

            </div>

            <div className="modal-movie-footer">
                <p>
                    Contact: email - ringler.brian@gmail.com<span> | </span> phone -
                    248-894-9966
                </p>
                <p><a href="https://github.com/brianRingler" target="_blank">GitHub</a></p>
            </div>
      </div>

    );
};

export default MovieDetail;