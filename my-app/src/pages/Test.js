import React, { useEffect, useState } from 'react';
import { getStorage, ref, getDownloadURL } from 'firebase/storage';

const Test = () => {
  const [audioUrl, setAudioUrl] = useState(null);

  useEffect(() => {
    // Replace 'your-audio-file.wav' with the actual path to your WAV file in Firebase Storage
    const audioFileRef = ref(getStorage(), 'video/audioFile1.wav');

    getDownloadURL(audioFileRef)
      .then(url => setAudioUrl(url))
      .catch(error => console.error('Error getting audio file URL:', error));
  }, []);

  const playAudio = () => {
    if (audioUrl) {
      const audio = new Audio(audioUrl);
      audio.play();
    }
  };

  return (
    <div>
      <h1>Audio Player</h1>
      {audioUrl ? (
        <>
          <button onClick={playAudio}>Play Audio</button>
          <p>Audio URL: {audioUrl}</p>
        </>
      ) : (
        <p>Loading audio...</p>
      )}
    </div>
  );
};

export default Test;
