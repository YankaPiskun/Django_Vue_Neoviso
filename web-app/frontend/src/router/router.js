import Main from '@/pages/Main';
import OrderVue from '@/pages/OrderVue';
import about from '@/pages/About';
import create from '@/pages/Create'
import employee from '@/pages/Employee'
import service from '@/pages/Service'
import orderID from '@/pages/OrderID'
import { createRouter, createWebHistory } from 'vue-router';

const routes=[
    {
        path: '/',
        component: Main
    },
    {
        path: '/OrderVue',
        component: OrderVue
    },
    {
        path: '/about',
        component: about
    },
    {
        path: '/create',
        component: create
    },
    {
        path: '/employee',
        component: employee
    },
    {
        path: '/service',
        component: service
    },
    {
        path: '/OrderVue/:id',
        component: orderID
    },
]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;