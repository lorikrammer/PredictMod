// Composables
import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue';

const routes = [
  {
    path: '/predictmod',
    component: Home,
    // XXX - Looks the below code chunk is automatically handled by
    //       this version (4.0.0 as of Jan 2024) of the Vue Router
    //       when nginx passes the $uri argument
    // beforeEnter: (to, from, next) => {
    //   const { uri } = to.query;
    //   console.log("===> Found URI: %s", uri);
    //   if (uri != null && uri != '/predictmod') {
    //     next(false);
    //     router.push(uri);
    //   } else {
    //     next();
    //   }
    // }
  },
  {
    path: '/predictmod/about',
    component: () => import('../views/About.vue'),
  },
  {
    path: '/predictmod/faq',
    component: () => import('../views/FAQ.vue'),
  }, {
    path: '/predictmod/contact',
    component: () => import('../views/Contact.vue'),
  },
    {
      path: '/predictmod/ehr-home', 
      component: () => import('../views/EHRHome.vue'),
    },
    {
      path: '/predictmod/mg-home', 
      component: () => import('../views/MGHome.vue'),
    },
    {
      path: '/predictmod/omics-home', 
      component: () => import('../views/OmicsHome.vue'),
    },
    {
      path: '/predictmod/users',
      component: () => import('@/views/Users.vue'),
    },
    {
      path: '/predictmod/login', 
      component: () => import('../views/Login.vue'),
    },
    {
      path: '/predictmod/help', 
      component: () => import('../views/Help.vue'),
    },
    {
      path: '/predictmod/query-builder', 
      component: () => import('../views/QueryBuilder.vue'),
    },
    {
      path: '/predictmod/testing', 
      component: () => import('../views/Testing.vue'),
    },
    {
      path: '/:pathMatch(.*)*',
      component: () => import('../views/NotFound.vue'),
    },
]

const router = createRouter({
  base: '/predictmod',
  history: createWebHistory(process.env.BASE_URL),
  // TODO: Might log useful information in the future(?)
  // watch: {
  //   '$route' (to, from) {
  //     console.log('Route changed from ' + from.path + ' to ' + to.path);
  //   },
  // },
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      }
    }
  },
  routes,
})

export default router
