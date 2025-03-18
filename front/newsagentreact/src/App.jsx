import React, { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import "./App.css";
import Button from "@mui/material/Button";
import { FormControl, InputLabel, MenuItem, Select } from "@mui/material";
import TextField from "@mui/material/TextField";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";
import Checkbox from "@mui/material/Checkbox";
import ListItemText from "@mui/material/ListItemText";
import OutlinedInput from "@mui/material/OutlinedInput";
import Skeleton from "@mui/material/Skeleton";
import logo from "../src/assets/logo-transparent.png";
import Grid from "@mui/material/Grid";

function App() {
  const [newstype, setNewsType] = useState("");
  const [query, setQuery] = useState("");
  const [source, setSource] = useState([]);
  const [category, setCategory] = useState("");
  const [fromdate, setFromDate] = useState("");
  const [toDate, setToDate] = useState("");
  const [sortby, setSortBy] = useState("");
  const [result, setResult] = useState({});
  const [error, setError] = useState("");
  const [showNews, setShowNews] = useState(false);
  const [loading, setLoading] = useState(true);
  const handleNewsTypeChange = (event) => {
    setNewsType(event.target.value);
  };
  const handleSortChange = (event) => {
    setSortBy(event.target.value);
  };
  const handleSourceChange = (event) => {
    console.log(event.target.value);
    setSource(event.target.value);
  };

  const handleSubmit = async () => {
    setLoading(true); // Yükleme başlatıldı
    const data = {
      newstype,
      query,
      source,
      category,
      fromdate,
      toDate,
      sortby,
    };

    try {
      const res = await fetch("http://localhost:5000/get-news", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      const news = await res.json();

      if (res.ok) {
        setShowNews(true);
        console.log(news.data);
        setResult(news.data);
        console.log(result);
        setError("");
      } else {
        setResult("");
        setError(news.error || "Bilinmeyen hata");
      }
    } catch (error) {
      setError("Bir hata oluştu!");
      setResult("");
      console.error(error);
    } finally {
      setLoading(false); // Yükleme tamamlandı
    }
  };
  return (
    <>
      <div className="fixed top-0 left-0 ">
        <img src={logo} alt="Logo" className=" logo" />
      </div>
      <div>
        <h1 className="text-center text-4xl my-2  ">Set your filters.</h1>
      </div>
      <div className="container">
        <div className="row my-5 ">
          <div className="col-3">
            <FormControl
              fullWidth
              color="light"
              className="color-white"
              style={{ color: "white" }}
            >
              <InputLabel id="demo-simple-select-label" color="white">
                News Type
              </InputLabel>
              <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={newstype}
                label="News Type"
                color="light"
                onChange={handleNewsTypeChange}
              >
                <MenuItem value="topheadlines">Top Headlines</MenuItem>
                <MenuItem value="everything">Everything</MenuItem>
              </Select>
            </FormControl>
          </div>
          <div className="col-3">
            <TextField
              id="outlined-basic"
              label="Query"
              variant="outlined"
              value={query}
              color="white"
              onChange={(event) => setQuery(event.target.value)}
            />
          </div>
          <div className="col-3">
            <FormControl sx={{ width: 300 }}>
              <InputLabel id="demo-multiple-checkbox-label">Source</InputLabel>
              <Select
                labelId="demo-multiple-checkbox-label"
                id="demo-multiple-checkbox"
                multiple
                value={source}
                onChange={handleSourceChange}
                input={<OutlinedInput label="Source" />}
                renderValue={(selected) => selected.join(", ")}
              >
                {sources.map((item) => (
                  <MenuItem key={item.title} value={item.title}>
                    <Checkbox checked={source.includes(item.title)} />
                    <ListItemText primary={item.title} />
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          </div>
          <div className="col-3">
            <TextField
              id="outlined-basic"
              label="Category"
              variant="outlined"
              value={category}
              onChange={(event) => setCategory(event.target.value)}
              disabled={source.length > 0}
            />
          </div>
        </div>
        <div className="row my-5">
          <div className="col-3">
            <TextField
              id="outlined-basic"
              label="From Date"
              type="date"
              variant="outlined"
              value={fromdate}
              onChange={(event) => setFromDate(event.target.value)}
              InputLabelProps={{
                shrink: true,
              }}
            />
          </div>
          <div className="col-3">
            <TextField
              id="outlined-basic"
              label="To Date"
              type="date"
              variant="outlined"
              value={toDate}
              onChange={(event) => setToDate(event.target.value)}
              InputLabelProps={{
                shrink: true,
              }}
            />
          </div>
          <div className="col-3">
            <FormControl fullWidth>
              <InputLabel id="demo-simple-select-label">Sort By</InputLabel>
              <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={sortby}
                label="sortby"
                onChange={handleSortChange}
              >
                <MenuItem value="relevancy">Relevancy</MenuItem>
                <MenuItem value="popularity">Popularity</MenuItem>
                <MenuItem value="publishedAt">PublishedAt</MenuItem>
              </Select>
            </FormControl>
          </div>
          <div className="col-3 p-2">
            <Button variant="contained" onClick={handleSubmit}>
              Search
            </Button>
          </div>
        </div>
      </div>
      <hr />
      {/* <div className="div">
        {showNews ? (
          loading ? (
            <div className="">
              {result
                .reduce((rows, key, index) => {
                  if (index % 3 === 0) rows.push([]);
                  rows[rows.length - 1].push(key);
                  return rows;
                }, [])
                .map((row, rowIndex) => (
                  <div className="row my-4" key={rowIndex}>
                    {row.map((item, index) => (
                      <div className="col-4" key={index}>
                        <Card sx={{ maxWidth: 700 }}>
                          <CardMedia
                            sx={{ height: 240 }}
                            image={item.urlToImg}
                            title={item.Headline}
                          />
                          <CardContent>
                            <Typography
                              gutterBottom
                              variant="h5"
                              component="div"
                              className="text-start"
                            >
                              {item.Headline}
                            </Typography>
                            <Typography
                              variant="body2"
                              sx={{ color: "text.secondary" }}
                              className="text-start"
                            >
                              {item.Summary}
                            </Typography>
                          </CardContent>
                          <CardActions
                            sx={{
                              display: "flex",
                              justifyContent: "space-between",
                            }}
                          >
                            <Button size="small" href={item.Link}>
                              Learn More
                            </Button>
                            <Typography
                              variant="body2"
                              sx={{ color: "text.secondary", ml: "auto" }}
                              className="pe-2 pb-2"
                            >
                              Source: {item.Source}
                            </Typography>
                          </CardActions>
                        </Card>
                      </div>
                    ))}
                  </div>
                ))}
            </div>
          ) : (
            <div className="">
              <div className="row my-4">
                <div className="col-4">
                  <Card sx={{ maxWidth: 700 }}>
                    <Skeleton variant="rectangular" width={700} height={240} />
                    <CardContent>
                      <Skeleton />
                      <Skeleton height={120} />
                    </CardContent>
                    <CardActions
                      sx={{ display: "flex", justifyContent: "space-between" }}
                    >
                      <Skeleton width="20%" />
                      <Skeleton width="20%" />
                    </CardActions>
                  </Card>
                </div>
                <div className="col-4">
                  <Card sx={{ maxWidth: 700 }}>
                    <Skeleton variant="rectangular" width={700} height={240} />
                    <CardContent>
                      <Skeleton />
                      <Skeleton height={120} />
                    </CardContent>
                    <CardActions
                      sx={{ display: "flex", justifyContent: "space-between" }}
                    >
                      <Skeleton width="20%" />
                      <Skeleton width="20%" />
                    </CardActions>
                  </Card>
                </div>
                <div className="col-4">
                  <Card sx={{ maxWidth: 700 }}>
                    <Skeleton variant="rectangular" width={700} height={240} />
                    <CardContent>
                      <Skeleton />
                      <Skeleton height={120} />
                    </CardContent>
                    <CardActions
                      sx={{ display: "flex", justifyContent: "space-between" }}
                    >
                      <Skeleton width="20%" />
                      <Skeleton width="20%" />
                    </CardActions>
                  </Card>
                </div>
              </div>
              <div className="row">
                <div className="col-4">
                  <Card sx={{ maxWidth: 700 }}>
                    <Skeleton variant="rectangular" width={700} height={240} />
                    <CardContent>
                      <Skeleton />
                      <Skeleton height={120} />
                    </CardContent>
                    <CardActions
                      sx={{ display: "flex", justifyContent: "space-between" }}
                    >
                      <Skeleton width="20%" />
                      <Skeleton width="20%" />
                    </CardActions>
                  </Card>
                </div>
                <div className="col-4">
                  <Card sx={{ maxWidth: 700 }}>
                    <Skeleton variant="rectangular" width={700} height={240} />
                    <CardContent>
                      <Skeleton />
                      <Skeleton height={120} />
                    </CardContent>
                    <CardActions
                      sx={{ display: "flex", justifyContent: "space-between" }}
                    >
                      <Skeleton width="20%" />
                      <Skeleton width="20%" />
                    </CardActions>
                  </Card>
                </div>
                <div className="col-4">
                  <Card sx={{ maxWidth: 700 }}>
                    <Skeleton variant="rectangular" width={700} height={240} />
                    <CardContent>
                      <Skeleton />
                      <Skeleton height={120} />
                    </CardContent>
                    <CardActions
                      sx={{ display: "flex", justifyContent: "space-between" }}
                    >
                      <Skeleton width="20%" />
                      <Skeleton width="20%" />
                    </CardActions>
                  </Card>
                </div>
              </div>
            </div>
          )
        ) : (
          <div></div>
        )}
      </div> */}
      {loading ? (
        <div className="">
          <div className="row my-4">
            <div className="col-4">
              <Card sx={{ maxWidth: 700 }}>
                <Skeleton variant="rectangular" width={700} height={240} />
                <CardContent>
                  <Skeleton />
                  <Skeleton height={120} />
                </CardContent>
                <CardActions
                  sx={{ display: "flex", justifyContent: "space-between" }}
                >
                  <Skeleton width="20%" />
                  <Skeleton width="20%" />
                </CardActions>
              </Card>
            </div>
            <div className="col-4">
              <Card sx={{ maxWidth: 700 }}>
                <Skeleton variant="rectangular" width={700} height={240} />
                <CardContent>
                  <Skeleton />
                  <Skeleton height={120} />
                </CardContent>
                <CardActions
                  sx={{ display: "flex", justifyContent: "space-between" }}
                >
                  <Skeleton width="20%" />
                  <Skeleton width="20%" />
                </CardActions>
              </Card>
            </div>
            <div className="col-4">
              <Card sx={{ maxWidth: 700 }}>
                <Skeleton variant="rectangular" width={700} height={240} />
                <CardContent>
                  <Skeleton />
                  <Skeleton height={120} />
                </CardContent>
                <CardActions
                  sx={{ display: "flex", justifyContent: "space-between" }}
                >
                  <Skeleton width="20%" />
                  <Skeleton width="20%" />
                </CardActions>
              </Card>
            </div>
          </div>
          <div className="row">
            <div className="col-4">
              <Card sx={{ maxWidth: 700 }}>
                <Skeleton variant="rectangular" width={700} height={240} />
                <CardContent>
                  <Skeleton />
                  <Skeleton height={120} />
                </CardContent>
                <CardActions
                  sx={{ display: "flex", justifyContent: "space-between" }}
                >
                  <Skeleton width="20%" />
                  <Skeleton width="20%" />
                </CardActions>
              </Card>
            </div>
            <div className="col-4">
              <Card sx={{ maxWidth: 700 }}>
                <Skeleton variant="rectangular" width={700} height={240} />
                <CardContent>
                  <Skeleton />
                  <Skeleton height={120} />
                </CardContent>
                <CardActions
                  sx={{ display: "flex", justifyContent: "space-between" }}
                >
                  <Skeleton width="20%" />
                  <Skeleton width="20%" />
                </CardActions>
              </Card>
            </div>
            <div className="col-4">
              <Card sx={{ maxWidth: 700 }}>
                <Skeleton variant="rectangular" width={700} height={240} />
                <CardContent>
                  <Skeleton />
                  <Skeleton height={120} />
                </CardContent>
                <CardActions
                  sx={{ display: "flex", justifyContent: "space-between" }}
                >
                  <Skeleton width="20%" />
                  <Skeleton width="20%" />
                </CardActions>
              </Card>
            </div>
          </div>
        </div>
      ) : (
        <div>
          {showNews && result?.length > 0 ? (
            <Grid container spacing={2}>
              {result.map((news, index) => (
                <Grid item xs={12} sm={6} md={4} key={index}>
                  <Card sx={{ maxWidth: 600 }}>
                    <CardMedia
                      sx={{ height: 250 }}
                      image={news.urlToImg}
                      title={news.Headline}
                    />
                    <CardContent>
                      <Typography
                        gutterBottom
                        variant="h6"
                        component="div"
                        className="text-start"
                      >
                        {news.Headline}
                      </Typography>
                      <Typography
                        variant="body2"
                        sx={{ color: "text.secondary" }}
                        className="text-start"
                      >
                        {news.Summary}
                      </Typography>
                    </CardContent>
                    <CardActions
                      sx={{
                        display: "flex",
                        justifyContent: "space-between",
                      }}
                    >
                      <Button size="small" href={news.Link}>
                        Learn More
                      </Button>
                      <Typography
                        variant="body2"
                        sx={{ color: "text.secondary", ml: "auto" }}
                        className="pe-2 pb-2"
                      >
                        Source: {news.Source}
                      </Typography>
                    </CardActions>
                  </Card>
                </Grid>
              ))}
            </Grid>
          ) : (
            <div>No news available</div>
          )}
        </div>
      )}
    </>
  );
}
const sources = [
  { title: "Any Source" },
  { title: "BBC" },
  { title: "CNN" },
  { title: "ESPN" },
  { title: "Fox News" },
  { title: "Google News" },
  { title: "MSNBC" },
  { title: "NBC News" },
  { title: "The New York Times" },
  { title: "The Wall Street Journal" },
  { title: "The Washington Post" },
];
export default App;
