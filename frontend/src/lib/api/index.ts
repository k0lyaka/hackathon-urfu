// Auto-generated lightweight API client for Urfu Hackathon Bot
// - Uses fetch and returns typed responses
// - Base URL can be provided, defaults to '' (same origin)

export type SubjectEnum =
  | "math"
  | "russian"
  | "physics"
  | "chemistry"
  | "biology"
  | "history"
  | "computer_science"
  | "foreign_language"
  | "literature";

export interface ExamScoreItem {
  subject: SubjectEnum;
  score: number; // 0..100
  year: number; // e.g. 2024
}

export interface AddExamScoresRequest {
  exams: ExamScoreItem[]; // 1..5 items
}

export interface ExamScoreDTO {
  id: number;
  subject: SubjectEnum;
  score: number;
  year: number;
}

export interface UserDTO {
  id: number;
  telegram_id: number;
  username: string | null;
  interest_tags: string[] | null;
  full_interest_text: string | null;
  exam_scores: ExamScoreDTO[];
}

export interface UpdateInterestsRequest {
  interests: string;
}

export interface SpecializationScore {
  id: number;
  minimal_score: number;
  year: number;
}

export interface Specialization {
  id: number;
  name: string;
  code: string;
  institute: string;
  tags: string[];
  scores: SpecializationScore[];
}

export interface CreateSpecializationScoreRequest {
  minimal_score: number;
  year: number;
}

export interface CreateSpecializationRequest {
  name: string;
  code: string;
  description: string;
  institute: string;
  scores: CreateSpecializationScoreRequest[];
}

export interface HTTPValidationError {
  detail?: Array<{ loc: (string | number)[]; msg: string; type: string }>;
}

export class ApiError extends Error {
  status: number;
  body: unknown;

  constructor(status: number, message: string, body: unknown) {
    super(message);
    this.status = status;
    this.body = body;
    Object.setPrototypeOf(this, ApiError.prototype);
  }
}

export class ApiClient {
  private baseUrl: string;
  private token: string;

  constructor(baseUrl: string, token: string) {
    this.baseUrl = baseUrl;
    this.token = token;
  }

  private headers(overrides?: Record<string, string>) {
    return {
      "Content-Type": "application/json",
      Authorization: this.token,
      ...(overrides || {}),
    } as HeadersInit;
  }

  private async request<T>(path: string, opts: RequestInit = {}): Promise<T> {
    const url = this.baseUrl + path;
    const res = await fetch(url, opts);
    const text = await res.text();
    let data: unknown = null;
    try {
      data = text ? JSON.parse(text) : null;
    } catch {
      // keep raw text when JSON parse fails
      data = text as unknown;
    }
    if (!res.ok) {
      throw new ApiError(
        res.status,
        res.statusText || `HTTP ${res.status}`,
        data
      );
    }
    return data as T;
  }

  // GET /profile -> UserDTO
  async getProfile(): Promise<UserDTO> {
    return this.request<UserDTO>(`/profile`, {
      method: "GET",
      headers: this.headers(),
    });
  }

  // POST /profile/exams -> UserDTO
  async addExamScores(body: AddExamScoresRequest): Promise<UserDTO> {
    return this.request<UserDTO>(`/profile/exams`, {
      method: "POST",
      headers: this.headers(),
      body: JSON.stringify(body),
    });
  }

  // POST /profile/interests -> UserDTO
  async updateInterests(body: UpdateInterestsRequest): Promise<UserDTO> {
    return this.request<UserDTO>(`/profile/interests`, {
      method: "POST",
      headers: this.headers(),
      body: JSON.stringify(body),
    });
  }

  // GET /specialization -> Specialization[]
  async getSpecializations(): Promise<Specialization[]> {
    return this.request<Specialization[]>(`/specialization`, {
      method: "GET",
      headers: this.headers(),
    });
  }

  // POST /specialization -> Specialization
  async createSpecialization(
    body: CreateSpecializationRequest
  ): Promise<Specialization> {
    return this.request<Specialization>(`/specialization`, {
      method: "POST",
      headers: this.headers(),
      body: JSON.stringify(body),
    });
  }
}

export default ApiClient;
export const defaultBaseUrl = import.meta.env.VITE_BASE_URL!;
