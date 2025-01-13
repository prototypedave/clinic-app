<template>
    <div v-if="error" class='fixed top-4 right-4 text-white p-4 rounded-md shadow-lg z-50 text-sm bg-red-500'>
        {{ error }}
    </div>
    <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
        <div>
            <h1 class="text-center text-2xl font-bold tracking-tight text-violet-950 hover:text-indigo-500">Afya Bora Clinic Management System</h1>
            <p class="text-center mt-2 text-sm font-medium tracking-tight text-violet-500">Welcome Back. Please Sign In to continue</p>
        </div>
        <div class="mt-6 sm:mx-auto sm:w-full sm:max-w-sm rounded-lg shadow-md border bg-violet-950 p-6 dark:border-gray-700">
            <form @submit.prevent="handleSignIn" class="space-y-6">
                <div>
                    <label for="email" class="block text-left text-sm/6 font-medium text-white">Email address</label>
                    <div class="mt-2">
                        <input id="email" name="email" type="email" v-model="email" placeholder="Enter your email" autocomplete="email" class="block w-full rounded-md border-0 pl-2 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm/6 bg-violet-200 placeholder-gray-400" />
                    </div>
                </div>
                <div>
                    <div class="flex items-center justify-between">
                        <label for="password" class="block text-left text-sm/6 font-medium text-white">Password</label>
                        <div class="text-sm">
                            <a href="/reset-password" class="font-semibold text-pink-600 hover:text-pink-500">Forgot password?</a>
                        </div>
                    </div>
                    <div class="mt-2">
                        <input id="password" name="password" v-model="password" placeholder="Enter your password" type="password" autocomplete="current-password" class="block w-full rounded-md border-0 pl-2 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm/6 bg-violet-200 placeholder-gray-400"/>
                    </div>
                </div>
                <div>
                    <button type="submit" class="flex w-full justify-center rounded-md bg-pink-600 px-3 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-pink-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
                </div>
            </form>
            <p class="mt-10 text-center text-sm text-white">Don't have an account? <a href="#" class="font-semibold text-pink-600 hover:text-pink-500">Contact Admin.</a></p>
        </div>
        <p class="text-center text-gray-500 text-xs mt-4">&copy;2024 Dave Tech. All rights reserved.</p>
    </div>
</template>

<script>
    import { useAuthStore } from '@/stores/auth'
    export default {
        data() {
            return {
                email: '',
                password: '',
            };
        },
        computed: {
            error() {
                const authStore = useAuthStore();
                return authStore.getError; 
            }
        },
        methods: {
            async handleSignIn() {
                const authStore = useAuthStore(); 
                try {
                    const success = await authStore.login({ email: this.email, password: this.password });
                    if (success) {
                      if (authStore.getRole === "admin") {
                          this.$router.push("/admin/dashboard");
                      } else {
                          this.$router.push("/dashboard");
                      }
                      
                    }
                } catch (err) {
                    console.error(err);
                    const authStore = useAuthStore();
                    authStore.error = err.message || 'An error occurred';

                    setTimeout(() => {
                        authStore.error = null;
                    }, 3000);
                }
            },

        },
    };
</script>