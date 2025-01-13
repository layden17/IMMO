module.exports = {
    mongodbMemoryServerOptions: {
      binary: {
        version: '7.0.3', // Set this to a compatible MongoDB version
        skipMD5: true,
      },
      instance: {},
      autoStart: false,
    },
  };
  