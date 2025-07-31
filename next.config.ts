import type { NextConfig } from "next";
import path from "path";

const nextConfig: NextConfig = {
  // Point to the frontend directory
  distDir: path.join(__dirname, 'frontend', '.next'),
  // Other config options
  experimental: {
    // Enable if needed
  }
};

export default nextConfig; 