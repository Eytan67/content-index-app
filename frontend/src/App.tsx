import { useState } from "react";
import "./App.css";

const App: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState<string>("");

  const handleSearch = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchQuery(event.target.value);
  };

  return (
    <div className="App">
      <h1>Content Index App</h1>
      <input
        type="text"
        placeholder="Search for lessons..."
        value={searchQuery}
        onChange={handleSearch}
      />
      <p>Searching for: {searchQuery}</p>
    </div>
  );
};

export default App;
