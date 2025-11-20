/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // If it's a static site
  trailingSlash: true,
  images: {
    unoptimized: true
  }
}

module.exports = nextConfig