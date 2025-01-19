<template>
    <div v-if="alert.visible" :class="{'fixed top-4 right-4 text-white p-4 rounded-md shadow-lg z-50 text-sm': true,
        'bg-green-500': !error,
        'bg-red-500': error
    }">
        {{ alert.message }}
    </div>
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-auto lg:py-0">
        <a href="#" class="flex items-center mb-4 text-2xl font-semibold mt-10">
            <div>
                <h1 class="text-center text-2xl font-bold tracking-tight text-violet-950 hover:text-indigo-500">Admin Registration</h1>
                <p class="text-center mt-2 text-sm font-medium tracking-tight text-violet-500">Please enter new password to continue</p>
            </div>
        </a>
        <div class="w-full bg-violet-950 rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0">
            <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                <form @submit.prevent="handlePasswordReset" class="space-y-4 md:space-y-4 text-indigo-100">
                    <div>
                        <label for="password" class="block mb-2 text-left text-sm font-medium">New Password</label>
                        <div class="relative">
                            <input v-model="password" :type="showPassword ? 'text' : 'password'" name="password" id="password" placeholder="************" class="bg-violet-200 text-violet-950 text-sm rounded-lg block w-full p-2.5" required @input='validateStrongPassword' />
                            <button type="button" @click="togglePassword" class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm text-indigo-400">
                                <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                                    <path d="M3.53 2.47a.75.75 0 0 0-1.06 1.06l18 18a.75.75 0 1 0 1.06-1.06l-18-18ZM22.676 12.553a11.249 11.249 0 0 1-2.631 4.31l-3.099-3.099a5.25 5.25 0 0 0-6.71-6.71L7.759 4.577a11.217 11.217 0 0 1 4.242-.827c4.97 0 9.185 3.223 10.675 7.69.12.362.12.752 0 1.113Z" />
                                    <path d="M15.75 12c0 .18-.013.357-.037.53l-4.244-4.243A3.75 3.75 0 0 1 15.75 12ZM12.53 15.713l-4.243-4.244a3.75 3.75 0 0 0 4.244 4.243Z" />
                                    <path d="M6.75 12c0-.619.107-1.213.304-1.764l-3.1-3.1a11.25 11.25 0 0 0-2.63 4.31c-.12.362-.12.752 0 1.114 1.489 4.467 5.704 7.69 10.675 7.69 1.5 0 2.933-.294 4.242-.827l-2.477-2.477A5.25 5.25 0 0 1 6.75 12Z" />
                                </svg>
                                <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                                    <path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" />
                                    <path fill-rule="evenodd" d="M1.323 11.447C2.811 6.976 7.028 3.75 12.001 3.75c4.97 0 9.185 3.223 10.675 7.69.12.362.12.752 0 1.113-1.487 4.471-5.705 7.697-10.677 7.697-4.97 0-9.186-3.223-10.675-7.69a1.762 1.762 0 0 1 0-1.113ZM17.25 12a5.25 5.25 0 1 1-10.5 0 5.25 5.25 0 0 1 10.5 0Z" clip-rule="evenodd" />
                                </svg>
                            </button>
                        </div>
                        <p v-if="strongError" class="text-red-500 text-sm mt-2">{{ strongError }}</p>
                    </div>
                    <div>
                        <label for="confirmPassword" class="block mb-2 text-left text-sm font-medium">Confirm New Password</label>
                        <div class="relative">
                            <input v-model="confirmPassword" :type="showPassword ? 'text' : 'password'" name="ConfirmPassword" id="confirmPassword" placeholder="************" class="bg-violet-200 text-violet-950 text-sm rounded-lg block w-full p-2.5" required @input='validatePassword' />
                            <button type="button" @click="togglePassword" class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm text-indigo-400">
                                <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                                    <path d="M3.53 2.47a.75.75 0 0 0-1.06 1.06l18 18a.75.75 0 1 0 1.06-1.06l-18-18ZM22.676 12.553a11.249 11.249 0 0 1-2.631 4.31l-3.099-3.099a5.25 5.25 0 0 0-6.71-6.71L7.759 4.577a11.217 11.217 0 0 1 4.242-.827c4.97 0 9.185 3.223 10.675 7.69.12.362.12.752 0 1.113Z" />
                                    <path d="M15.75 12c0 .18-.013.357-.037.53l-4.244-4.243A3.75 3.75 0 0 1 15.75 12ZM12.53 15.713l-4.243-4.244a3.75 3.75 0 0 0 4.244 4.243Z" />
                                    <path d="M6.75 12c0-.619.107-1.213.304-1.764l-3.1-3.1a11.25 11.25 0 0 0-2.63 4.31c-.12.362-.12.752 0 1.114 1.489 4.467 5.704 7.69 10.675 7.69 1.5 0 2.933-.294 4.242-.827l-2.477-2.477A5.25 5.25 0 0 1 6.75 12Z" />
                                </svg>
                                <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
                                    <path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" />
                                    <path fill-rule="evenodd" d="M1.323 11.447C2.811 6.976 7.028 3.75 12.001 3.75c4.97 0 9.185 3.223 10.675 7.69.12.362.12.752 0 1.113-1.487 4.471-5.705 7.697-10.677 7.697-4.97 0-9.186-3.223-10.675-7.69a1.762 1.762 0 0 1 0-1.113ZM17.25 12a5.25 5.25 0 1 1-10.5 0 5.25 5.25 0 0 1 10.5 0Z" clip-rule="evenodd" />
                                </svg>
                            </button>
                        </div>
                        <p v-if="passError" class="text-red-500 text-sm mt-2">{{ passError }}</p>
                    </div>
                    <button type="submit" class="w-full text-white bg-indigo-500 hover:bg-indigo-600 focus:ring-4 focus:outline-none focus:ring-indigo-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center ">Create an account</button>
                </form>
            </div>
        </div>
    </div>
    
</template>

<script>
import { useTokenStore } from '@/stores/resetToken';

export default {
    data() {
        return {
            password: "",
            confirmPassword: "",
            strongError: "",
            passError: "",
            showPassword: false,
            alert: { visible: false, message: '' },
            error: false,
        };
    },
    
    methods: {
        validateStrongPassword () {
            const strongPass = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]+$/;
            if (this.password.length < 8 && this.password != "") {
                this.strongError = "Password length should be 8 or more!";
            } else if (!strongPass.test(this.password) && this.password != "") {
                this.strongError = "Pasword should have atleast have an UPPERCASE and lowercase character, a number and special character";
            } else {
                this.strongError = "";
            }
        },

        validatePassword () {
            if (this.password != this.confirmPassword) {
                this.passError = "Password doesnt match"
            }
            else {
                this.passError = "";
            }
        },

        togglePassword() {
            this.showPassword = !this.showPassword;
        },

        showAlert(message, error) {
            this.error = error;
            this.alert.visible = true; 
            this.alert.message = message;
            this.$nextTick(() => { 
                setTimeout(() => {
                    this.alert.visible = false;
                }, 3000); 
            });
        },

        resetForm() {
            this.password = "";
            this.confirmPassword = "";
            this.strongError = "";
            this.passError = "";
            this.showPassword = false;
            this.alert.visible = false;
            this.alert.message = '';
            this.error = false;
        },

        async handlePasswordReset() {
            const tokenStore = useTokenStore();
            try {
                const response = await fetch(`http://localhost:8000/users/password-reset/${tokenStore.token}/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        token: this.resetToken,
                        password: this.password,
                        confirm_password: this.confirmPassword,
                    }),
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    const errorMessage = errorData.message || 'An unknown error occurred';
                    this.error = true;
                    this.showAlert(errorMessage, true);
                    this.resetForm();
                    return;
                }

                const data = await response.json();
                this.showAlert(data.message, false); 
                setTimeout(() => {
                    this.$router.push({ name: 'sign-in' });
                    this.resetForm();
                }, 3000); 
                
            } catch (error) {
                let status = 410;
                if (error.message === "Failed to fetch") {
                    status = 503;
                }

                this.$router.push({
                    name: 'not-found',
                    query: { message: error.message, origin: this.$route.fullPath, status: status },
                });
                this.resetForm();
            }
        },
    },
};
</script>