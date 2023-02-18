<template>
    <div class="app-loader">
        <div class="spin-wrapper">
            <div class="spinner"></div>
            <div class="spinner__text">Loading...</div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
    .app-loader {
        width: 100vw;
        height: 100vh;
        position: fixed;
        background: rgba(127, 127, 127, 0.5);
        z-index: 1000;

        .spin-wrapper {
            display: flex;
            height: 100%;
            flex-direction: column;
            justify-content: center;
            align-items: center;

            .spinner{
                height: 60px;
                width: 60px;
                border: 3px solid transparent;
                border-top-color: #A04668;
                border-radius: 50%;
                animation: spin 2s linear infinite;
                
                &__text {
                    margin-top: 50px;
                }

                &:before, &:after{
                    content:'';
                    position: absolute;
                    border: 3px solid transparent;
                    border-radius: 50%;
                }
                
                &:before{
                    border-top-color: #254E70;
                    top: -12px;
                    left: -12px;
                    right: -12px;
                    bottom: -12px;
                    animation: spin 3s linear infinite;
                }
                
                &:after{
                    border-top-color: #141314;
                    top: 6px;
                    left: 6px;
                    right: 6px;
                    bottom: 6px;  
                    animation: spin 4s linear infinite;
                }
            }
        }

        @keyframes spin{
            0% {transform: rotate(0deg);}
            100% {transform: rotate(360deg);}
        }
    }
</style>