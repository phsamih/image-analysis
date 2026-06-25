import axios from "axios";
export const API_BASE = import.meta.env.VITE_API_BASE || "";
export async function analyzeImage(file) {
  const formData = new FormData();
  formData.append("file", file);
  const res = await axios.post(`${API_BASE}/api/analyze`, formData, { headers: { "Content-Type": "multipart/form-data" } });
  return res.data;
}
export async function fetchProjects() {
  const res = await axios.get(`${API_BASE}/api/projects`);
  return res.data;
}
