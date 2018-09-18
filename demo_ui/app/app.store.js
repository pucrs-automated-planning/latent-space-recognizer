import { observable, action } from "mobx";
import AppSession from "./session/app";

export default class AppStore {

    @observable initialized = false;

    appSession = AppSession.getInstance();

    @action async initialize() {
        console.log("Initializing Application...");
        await this.appSession.initialize();
        console.log("All sessions initialized.");
        this.initialized = true;
    }
}