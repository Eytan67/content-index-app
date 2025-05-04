import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

interface Lesson {
  id: number;
  title: string;
  content: string;
  file_path: string;
  creator_name: string;
}

function App() {
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/lessons")
      .then((response) => {
        setLessons(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching lessons:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <h1>Content Index</h1>
      <h2>Lessons</h2>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {lessons.map((lesson) => (
            <li key={lesson.id}>
              <h3>{lesson.title}</h3>
              <p>{lesson.content}</p>
              <p>By: {lesson.creator_name}</p>
              <a
                href={`http://127.0.0.1:8000/${lesson.file_path}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                View Lesson
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
