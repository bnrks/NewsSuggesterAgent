import { useState } from "react";

export default function NewsForm() {
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("");
  const [source, setSource] = useState("");
  const [timeRange, setTimeRange] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const requestData = {
      query,
      category,
      source,
      time_range: timeRange,
    };

    try {
      const response = await fetch("http://localhost:8000/recommendations", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestData),
      });

      if (response.ok) {
        const data = await response.json();
        alert("Haberler başarıyla alındı!");
        console.log(data);
      } else {
        alert("Bir hata oluştu.");
      }
    } catch (error) {
      console.error("Hata:", error);
      alert("Bağlantı kurulamadı.");
    }
  };

  return (
    <>
      <div className="container mt-5">
        <h1 className="mb-4">🔎 Haber Öneri Sistemi</h1>
        <form onSubmit={handleSubmit}>
          {/* Query */}
          <div className="mb-3">
            <label htmlFor="query" className="form-label">
              Arama Terimi:
            </label>
            <input
              type="text"
              className="form-control"
              id="query"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              required
            />
          </div>

          {/* Category */}
          <div className="mb-3">
            <label htmlFor="category" className="form-label">
              Kategori:
            </label>
            <select
              className="form-select"
              id="category"
              value={category}
              onChange={(e) => setCategory(e.target.value)}
              required
            >
              <option value="">Kategori Seçin</option>
              <option value="technology">Teknoloji</option>
              <option value="sports">Spor</option>
              <option value="politics">Politika</option>
              <option value="entertainment">Eğlence</option>
            </select>
          </div>

          {/* Source */}
          <div className="mb-3">
            <label htmlFor="source" className="form-label">
              Kaynak:
            </label>
            <select
              className="form-select"
              id="source"
              value={source}
              onChange={(e) => setSource(e.target.value)}
              required
            >
              <option value="">Kaynak Seçin</option>
              <option value="bbc">BBC</option>
              <option value="cnn">CNN</option>
              <option value="reuters">Reuters</option>
              <option value="nytimes">New York Times</option>
            </select>
          </div>

          {/* Time Range */}
          <div className="mb-3">
            <label className="form-label">Zaman Aralığı:</label>
            <div className="form-check">
              <input
                type="radio"
                className="form-check-input"
                id="current"
                value="current"
                checked={timeRange === "current"}
                onChange={() => setTimeRange("current")}
              />
              <label className="form-check-label" htmlFor="current">
                Güncel Haberler
              </label>
            </div>
            <div className="form-check">
              <input
                type="radio"
                className="form-check-input"
                id="all"
                value="all"
                checked={timeRange === "all"}
                onChange={() => setTimeRange("all")}
              />
              <label className="form-check-label" htmlFor="all">
                Geçmiş ve Güncel Haberler
              </label>
            </div>
          </div>

          {/* Submit Button */}
          <button type="submit" className="btn btn-primary w-100">
            Haberleri Getir
          </button>
        </form>
      </div>
    </>
  );
}
