import axios from "axios";
import { MeganJohns } from "./types/MeganJohns";

const baseURL = import.meta.env.VITE_API_URL as string;

const api = axios.create({ baseURL: baseURL });

export const getMeganJohns = async (): Promise<MeganJohns> => {
  const response = await api.get<MeganJohns>("/");
  return response.data as MeganJohns;
};
