<template>
    <div v-if="alert.visible" :class="{'fixed top-4 right-4 text-white p-4 rounded-md shadow-lg z-50 text-sm': true,
        'bg-green-500': !error,
        'bg-red-500': error
    }">
        {{ alert.message }}
    </div>
    <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
        <div>
            <h1 class="text-center text-2xl font-bold tracking-tight text-violet-950 hover:text-indigo-500">Afya Bora Clinic Management System</h1>
            <p class="text-center mt-2 text-sm font-medium tracking-tight text-violet-500">Forgot your password? Dont worry enter your email to continue..</p>
        </div>
        <div class="mt-6 sm:mx-auto sm:w-full sm:max-w-sm rounded-lg shadow-md border bg-violet-950 p-6 dark:border-gray-700">
            <form @submit.prevent="handlePasswordReset" class="space-y-6">
                <div>
                    <label for="email" class="block text-left text-sm/6 font-medium text-white">Email address</label>
                    <div class="mt-2">
                        <input id="email" name="email" type="email" v-model="email" placeholder="Enter your email" autocomplete="email" class="block w-full rounded-md border-0 pl-2 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm/6 bg-violet-200 placeholder-gray-400" />
                    </div>
                </div>
                <div>
                    <button type="submit" class="flex w-full justify-center rounded-md bg-pink-600 px-3 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-pink-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Reset Password</button>
                </div>
            </form>
            <p class="mt-10 text-center text-sm text-white">If the email is registered you will receive a link to reset your password</p>
        </div>
        <p class="text-center text-gray-500 text-xs mt-4">&copy;2024 Dave Tech. All rights reserved.</p>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                email: '',
                error: false,
                alert: { visible: false, message: '' },
            };
        },
        methods: {
            showAlert(message, error) {
                this.error = error;
                this.alert = { visible: true, message };
                setTimeout(() => {
                    this.alert.visible = false;
                }, 3000); 
            },

            resetForm () {
                this.email = "";
                this.error = false;
                this.alert.visible = false;
                this.alert.message = "";
            },

            async handlePasswordReset() {
                try {
                    const email = this.email;
                    const response = await fetch("http://127.0.0.1:8000/users/send-link", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({ email }),
                    });

                    if (!response.ok) {
                        const errorData = await response.json();
                        this.showAlert(errorData.error || 'An unknown error occurred', true);
                        return;
                    }

                    const data = await response.json();
                    this.showAlert(data.message, false);
                    setTimeout(() => {
                        this.$router.push({ name: 'sign-in' });
                        this.resetForm();
                    }, 2000); 
                } catch (error) {
                    let status = 410;
                    if (error.message === "Failed to fetch") {
                        status = 503;
                    }

                    this.$router.push({
                        name: 'ServerError',
                        query: { message: error.message, origin: this.$route.fullPath, status: status },
                    });
                    this.resetForm();
                }
            },
        },
    };
</script>