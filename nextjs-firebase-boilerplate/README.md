# Next.js 13 Firebase Starter

## IMPORTANT: READ THROUGH THIS README TO UNDERSTAND HOW TO USE IT
This is a starter template for building Next.js 13 applications with Firebase. It provides a solid foundation for developing modern web applications with server-side rendering, authentication, and real-time data synchronization.

## Features

- Next.js 13: Build powerful and scalable server-side rendered React applications.
- Firebase: Leverage the Firebase platform for authentication, real-time database, and cloud functions.
- Tailwind CSS: Rapidly build custom user interfaces using the utility-first CSS framework.
- Automatic Code Splitting: Optimize performance by splitting your JavaScript code into smaller, cacheable chunks.
- Dynamic Routing: Create dynamic routes for handling different pages and content.
- Hot Module Replacement: Enjoy a fast development experience with hot module replacement for instant code changes.
- Environment Variables: Safely manage environment-specific configuration values using environment variables.
- ESLint and Prettier: Maintain code quality and consistency with the help of ESLint and Prettier.

## Prerequisites

Before getting started, ensure you have the following prerequisites:

- Node.js 14 or higher
- npm or yarn package manager

## Getting Started

- Navigate into the project directory: `cd nextjs-firebase-boilerplate`
- Install the dependencies:

```bash
  npm install
  # or
  yarn install
```

- Run the development server:

```bash
  npm run dev
  # or
  yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result. There would be errors initially since we haven't set up Firestore on Firebase yet.

Note: Please follow the instructions on the doc provided (tinyurl.com/hwap-docs) to set up your Firebase project.

You can start editing the page by modifying `app/page.js`. The page auto-updates as you edit the file. This is one of the advantage of Next.js since it has built-in routers. 

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Set Up Firebase

<https://console.firebase.google.com/>

Example...

What you will see on Firebase:
```Javascript
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "your_api_key",
  authDomain: "your_auth_domain",
  projectId: "your_project_id",
  storageBucket: "your_storage_bucket",
  messagingSenderId: "your_messaging_sender_id",
  appId: "your_app_id"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
```
Copy and paste the config strings into your `.env` file which should look like the following:

```md
FIREBASE_API_KEY=your_api_key
FIREBASE_AUTH_DOMAIN=your_auth_domain
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_STORAGE_BUCKET=your_storage_bucket
FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
FIREBASE_APP_ID=your_app_id
```

You should now be setup to use Firebase.

## Authentication

- In `src/firebase` directory, exists the directory `auth` containing the logic for `signin` and `signup`.

## Folder Structure

The folder structure of this project is organized as follows:

- `pages`: Contains the Next.js pages for server-side rendering.
- `components`: Holds the reusable React components.
- `lib`: Includes utility functions and modules.
- `public`: Stores static assets such as images, fonts, and stylesheets.
- `styles`: Contains global styles and Tailwind CSS configuration.
- `firebase`: Houses the Firebase configuration and Firebase-related functions.

Feel free to modify and expand the folder structure according to your project requirements.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.

## Deployment

To deploy your Next.js application with Firebase, follow the Firebase deployment instructions specific to your hosting option (Firebase Hosting, Cloud Functions, etc.). Make sure to set up the appropriate environment variables for your production environment.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

This project was created using the Next.js framework and Firebase platform.

Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [Firebase Documentation](https://firebase.google.com/docs)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
