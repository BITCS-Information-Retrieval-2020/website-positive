import axios from "axios";

const axiosInstance = axios.create(
  {
    baseURL: 'http://localhost:8090/polls',
    timeout: 1000
  }
);
export default axiosInstance;
