import { observable } from "mobx";

export default class AppSession {

    static instance = null;

    static getInstance() {
        if (AppSession.instance == null) AppSession.instance = new AppSession();

        return AppSession.instance;
    }

    async initialize() {

    }

    @observable to = null;


}