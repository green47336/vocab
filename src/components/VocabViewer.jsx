import React, { useState } from "react";
import vocab from "../data/vocab.json";

const VocabViewer = () => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [showDetails, setShowDetails] = useState(false);

  const currentTerm = vocab[currentIndex];

  const handleTermClick = () => {
    setShowDetails(!showDetails);
  };

  const handleNext = () => {
    setShowDetails(false);
    setCurrentIndex((prevIndex) => (prevIndex + 1) % vocab.length);
  };

  return (
    <div
      style={{
        fontFamily: "Arial, sans-serif",
        padding: "20px",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "100vh",
        textAlign: "center",
      }}
    >
      <h1>Vocab Viewer</h1>
      <div
        onClick={handleTermClick}
        style={{
          cursor: "pointer",
          padding: "10px",
          border: "1px solid #ccc",
          borderRadius: "5px",
          marginBottom: "10px",
          width: "300px",
        }}
      >
        <strong>{currentTerm.term}</strong>
      </div>
      {showDetails && (
        <div style={{ marginBottom: "10px", width: "300px" }}>
          <p>
            <strong>Definition:</strong> {currentTerm.definition}
          </p>
          <p>
            <strong>Creator:</strong> {currentTerm.creator || ""}
          </p>
          <p>
            <strong>Year:</strong> {currentTerm.year || ""}
          </p>
        </div>
      )}
      <button onClick={handleNext} style={{ padding: "10px 20px" }}>
        Next Term
      </button>
    </div>
  );
};

export default VocabViewer;
