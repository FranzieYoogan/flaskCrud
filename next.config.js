/** @type {import('next').NextConfig} */
const nextConfig = {
  rewrites: async () => {
    return [
      {
        source: '/api/:path*',
        destination:
          process.env.NODE_ENV === 'development'
            ? 'http://localhost:3301/api/:path*'
            : '/api/',
      },
    ]
  },
}

module.exports = nextConfig
